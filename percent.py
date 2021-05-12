def main():
    def percent_Plus():

        def percent_change(percent,whole):

            return ((percent * whole) / 100.00) + whole


        percent = float(input("Enter Percentage: "))
        whole = float(input("Enter last price: "))

        number = percent_change(percent,whole)
        print(number)
        main()

    def percent_minus():
        def percent_change(percent,whole):

            return whole - ((percent * whole) / 100.00)


        percent = float(input("Enter Percentage: "))
        whole = float(input("Enter last price: "))

        number = percent_change(percent,whole)
        print(number)
        main()

    def percentage_of():
        def percent_change(lower_number,whole):
            return (100 - (lower_number / whole) * 100)



        whole = float(input("Enter the whole number: "))
        lower_number = float(input("Enter the lower number to calculate percentage of whole: "))

        number = percent_change(lower_number,whole)

        print(number)
        main()

    ask = int(input("Please enter 1 for percent_plus, 2 for percent_minus or 3 for percentage_of: (0 to exit) "))

    if ask == 1:
        percent_Plus()
    elif ask == 2:
        percent_minus()
    elif ask == 3:
        percentage_of()
    elif ask == 0:
        exit()
    else:
        print("Wrong selection")
        main()
main()

if __name__ == '__main__':
    main()