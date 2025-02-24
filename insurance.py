def calculate_insurance_period(days):
    """
    Calculate Months and Days of Insurance based on 25:30 reduction
    Υπολογίζει τους μήνες και τις ημέρες ασφάλισης με βάση την αναγωγή 25:30

    Args:
        days (float): Οι πραγματικές ημέρες ασφάλισης
        
    Returns:
        tuple: (μήνες, ημέρες)
    """

    # if 25 days = 30 days, then x days = (x * 30) / 25
    # Αν 25 ημέρες = 30 ημέρες, τότε x ημέρες = (x * 30) / 25
    adjusted_days = (days * 30) / 25
    
    # Calculate full months
    # Υπολογίζουμε τους πλήρεις μήνες
    months = int(adjusted_days // 30)
    
    # Calculate remaining days
    # Υπολογίζουμε τις υπόλοιπες ημέρες
    remaining_days = round(adjusted_days % 30, 1)
    
    return months, remaining_days

def main():
    while True:
        try:
            # ask user to input days
            # Ζητάμε από τον χρήστη να εισάγει τις ημέρες
            user_input = input("\nΕισάγετε τις ημέρες ασφάλισης (ή 'q' για έξοδο): ")
            
            # check for exit the program
            # Έλεγχος για έξοδο
            if user_input.lower() == 'q':
                print("Το πρόγραμμα τερματίστηκε.")
                break
            
            # Convert input to number
            # Μετατροπή της εισόδου σε αριθμό
            days = float(user_input)
            
            # Check for negative days
            # Έλεγχος για αρνητικές ημέρες
            if days < 0:
                print("Παρακαλώ εισάγετε θετικό αριθμό ημερών.")
                continue
            
            # Calculate insurance period
            # Υπολογισμός περιόδου ασφάλισης
            months, remaining_days = calculate_insurance_period(days)
            
            # Print results
            # Εκτύπωση αποτελεσμάτων
            print(f"\nΟι {days} ημέρες ασφάλισης αντιστοιχούν σε:")
            print(f"{months} μήνες και {remaining_days} ημέρες")
            
        except ValueError:
            print("Παρακαλώ εισάγετε έναν έγκυρο αριθμό.") # Please enter a valid number
        except Exception as e:
            print(f"Προέκυψε σφάλμα: {str(e)}")

if __name__ == "__main__":
    print("Πρόγραμμα υπολογισμού περιόδου ασφάλισης") # Insurance period calculation program
    print("Σημείωση: Η αναγωγή γίνεται με βάση τον κανόνα 25:30 ημερών") # Note: The reduction is based on the 25:30 days rule
    main()