import tkinter as tk
from tkinter import ttk, messagebox
import re

class InsuranceCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Υπολογισμός Ημερών Ασφάλισης")
        self.root.geometry("600x450")
        
        # Στυλ
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        self.style.configure('Info.TLabel', font=('Arial', 9, 'italic'))
        
        # Frame για το περιεχόμενο
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Τίτλος
        title_label = ttk.Label(main_frame, 
                              text="Υπολογισμός Περιόδου Ασφάλισης",
                              style='Header.TLabel')
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Επιλογή τύπου υπολογισμού
        self.calculation_type = tk.StringVar(value="public")
        
        ttk.Label(main_frame, 
                 text="Επιλέξτε τύπο υπολογισμού:",
                 style='TLabel').grid(row=1, column=0, pady=10, sticky=tk.W)
        
        # Frame για τις επιλογές υπολογισμού
        calc_frame = ttk.Frame(main_frame)
        calc_frame.grid(row=2, column=0, columnspan=2, pady=5, sticky=tk.W)
        
        # Ραδιοκουμπιά για τις τρεις επιλογές
        ttk.Radiobutton(calc_frame, 
                       text="Δημόσιο (30 ημέρες)", 
                       variable=self.calculation_type,
                       value="public").grid(row=0, column=0, padx=10, sticky=tk.W)
        
        ttk.Radiobutton(calc_frame, 
                       text="Ιδιωτικό (αναγωγή 25->30)", 
                       variable=self.calculation_type,
                       value="private_adjusted").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        
        ttk.Radiobutton(calc_frame, 
                       text="Ιδιωτικό (25 ημέρες)", 
                       variable=self.calculation_type,
                       value="private_25").grid(row=2, column=0, padx=10, sticky=tk.W)
        
        # Επεξηγηματικό κείμενο
        info_text = ("Δημόσιο: Υπολογισμός με βάση τις 30 ημέρες\n"
                    "Ιδιωτικό με αναγωγή: Μετατροπή από 25 σε 30 ημέρες\n"
                    "Ιδιωτικό χωρίς αναγωγή: Υπολογισμός με βάση τις 25 ημέρες")
        ttk.Label(main_frame, 
                 text=info_text,
                 style='Info.TLabel').grid(row=3, column=0, columnspan=2, pady=10)
        
        # Είσοδος ημερών
        ttk.Label(main_frame, 
                 text="Εισάγετε ημέρες ασφάλισης:",
                 style='TLabel').grid(row=4, column=0, pady=10, sticky=tk.W)
        
        self.days_entry = ttk.Entry(main_frame, width=20)
        self.days_entry.grid(row=4, column=1, pady=10, sticky=tk.W)
        
        # Κουμπί υπολογισμού
        calculate_btn = ttk.Button(main_frame, 
                                 text="Υπολογισμός",
                                 command=self.calculate)
        calculate_btn.grid(row=5, column=0, columnspan=2, pady=20)
        
        # Πλαίσιο αποτελεσμάτων
        self.result_frame = ttk.LabelFrame(main_frame, text="Αποτελέσματα", padding="10")
        self.result_frame.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        self.result_label = ttk.Label(self.result_frame, text="")
        self.result_label.grid(row=0, column=0, pady=5)

    def calculate_insurance_period(self, days, calc_type):
        """
        Υπολογίζει τους μήνες και τις ημέρες ασφάλισης ανάλογα με τον τύπο υπολογισμού
        """
        if calc_type == "public":
            # Για δημόσιο (30 ημέρες)
            adjusted_days = days
            base_days = 30
        elif calc_type == "private_adjusted":
            # Για ιδιωτικό με αναγωγή 25->30
            adjusted_days = (days * 30) / 25
            base_days = 30
        else:  # private_25
            # Για ιδιωτικό χωρίς αναγωγή (25 ημέρες)
            adjusted_days = days
            base_days = 25
        
        months = int(adjusted_days // base_days)
        remaining_days = round(adjusted_days % base_days, 1)
        
        return months, remaining_days, base_days

    def calculate(self):
        """Χειρίζεται τον υπολογισμό και την εμφάνιση αποτελεσμάτων"""
        try:
            # Έλεγχος εγκυρότητας εισόδου
            days_input = self.days_entry.get()
            if not re.match(r'^\d*\.?\d+$', days_input):
                raise ValueError("Παρακαλώ εισάγετε έναν έγκυρο αριθμό.")
            
            days = float(days_input)
            if days < 0:
                raise ValueError("Παρακαλώ εισάγετε θετικό αριθμό ημερών.")
            
            # Υπολογισμός
            months, remaining_days, base_days = self.calculate_insurance_period(
                days, 
                self.calculation_type.get()
            )
            
            # Εμφάνιση αποτελεσμάτων
            result_text = f"Οι {days} ημέρες ασφάλισης αντιστοιχούν σε:\n"
            result_text += f"{months} μήνες και {remaining_days} ημέρες"
            result_text += f"\n(με βάση τις {base_days} ημέρες ανά μήνα)"
            self.result_label.config(text=result_text)
            
        except ValueError as e:
            messagebox.showerror("Σφάλμα", str(e))
        except Exception as e:
            messagebox.showerror("Σφάλμα", f"Προέκυψε σφάλμα: {str(e)}")

def main():
    root = tk.Tk()
    app = InsuranceCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()