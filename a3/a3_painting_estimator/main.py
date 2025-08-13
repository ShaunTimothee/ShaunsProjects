import functions as f
    
def main():
    f.get_requirements()
    answer = "y"
        
    while answer == "y":
        f.estimate_painting_costs()
            
        answer = input("\nEstimate another paint job? (y/n): ")
            
        if answer == "n":
            print("Thank you for using our Painting Estimator!")
            break
            
if __name__ == "__main__":
        main()