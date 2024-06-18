import pandas as pd

# Load the shoe prices dataset
df = pd.read_csv('shoes_data.csv')

def chatbot():
    print("\n" + "="*35)
    print("||  Welcome to Shoe Information Chatbot  ||")
    print("="*35)
    
    while True:
        print("\nWhat would you like to know about shoes?")
        print("="*40)
        print("||  1. Shoe count by gender             ||")
        print("||  2. Top 10 brands                    ||")
        print("||  3. Most popular model by brand      ||")
        print("||  4. Top 10 most sold types           ||")
        print("||  5. Top 10 most sold materials       ||")
        print("||  6. Search for a specific shoe       ||")
        print("||  7. Exit                             ||")
        print("="*40)
        
        user_input = input("Enter the number of your choice: ")
        
        if user_input == '1':
            gender = df['Gender'].value_counts().reset_index().rename(columns={'index': 'Gender', 'Gender': 'count'})
            print("="*40)
            print("||  Shoe Count by Gender:              ||")
            print("="*40)
            print(gender)
        elif user_input == '2':
            brand = df['Brand'].value_counts().reset_index().rename(columns={'index': 'Brand', 'Brand': 'count'})
            print("="*40)
            print("||  Top 10 Brands:                     ||")
            print("="*40)
            print(brand.head(10))
        elif user_input == '3':
            brand_model_count = df.groupby(['Brand', 'Model']).size().reset_index(name='count').sort_values('count', ascending=False)
            brand_model_count = brand_model_count.groupby('Brand').head(1).reset_index(drop=True)
            print("="*40)
            print("||  Most Popular Model by Brand:       ||")
            print("="*40)
            print(brand_model_count)
        elif user_input == '4':
            type_price = df.groupby('Type')['Price (USD)'].sum().reset_index().sort_values('Price (USD)', ascending=False).head(10)
            print("="*40)
            print("||  Top 10 Most Sold Types:            ||")
            print("="*40)
            print(type_price)
        elif user_input == '5':
            material_price = df.groupby('Material')['Price (USD)'].sum().reset_index().sort_values('Price (USD)', ascending=False).head(10)
            print("="*40)
            print("||  Top 10 Most Sold Materials:        ||")
            print("="*40)
            print(material_price)
        elif user_input == '6':
            search_shoe()
        elif user_input == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please choose a valid option.")

def search_shoe():
    brand = input("Enter the brand of the shoe(make sure to input it correctly example: >>nike<<-- this is wrong || >>Nike<<--This is Right): ")
    color = input("Enter the color of the shoe(same goes here): ")
    
    filtered_shoe = df[(df['Brand'] == brand) & (df['Color'].str.contains(color, case=False, regex=False))]
    if not filtered_shoe.empty:
        result = filtered_shoe[['Model', 'Price (USD)']]
        print("="*40)
        print("||  Search Results:                     ||")
        print("="*40)
        print(result)
    else:
        print("No matching shoe found.")

if __name__ == "__main__":
    chatbot()
