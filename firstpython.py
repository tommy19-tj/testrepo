user_a = input('Hi how can I assist you today?\n' #customer is prompted to select what service they need done on vehicle
               'Select from the following:'       #customer will select from the following list
               '\nA) Fill tank with gas'
               '\nB) Get an oil change'
               '\nC) Get wipers changed'
               '\nD) Get brake fluid inspected'
               '\nE) Get tires rotated'
               '\nMake a selection:\t')
########################################################################################################################
############################################# Start off right here #####################################################
############################################ Decision statement ########################################################
    if user_a == 'A' or 'a': # this line tests to see if the user has entered a capital or lower case a
        op_1 = float(input('How many gallons does your tank hold?\t'))

        if op_1 <= 7.5: # Use this value if user input is less than or equal to 7.5
            price = 3.5 # Set price of price variable
            ttl = (price * 0.25) + (price) # total amount of price and user input
            print('Total Amount Due: ' + '${:,.2f}'.format(ttl))
        elif op_1 >= 6 and op_1 <= 10:
            price = 2.50
            ttl = (price * 0.50) + price
            print('Total Amount Due: ' + '${:,.2f}'.format(ttl))
        elif op_1 >= 11 and op_1 <= 20:
            price = 3.50
            ttl = (price * 0.75) + price
            print('Total Amount Due: ' + '${:,.2f}'.format(ttl))
########################################################################################################################
################# This section of code configures the type of oil service the customer will ############################
################################################# get ##################################################################
elif user_a == 'B' or 'b': # this line tests to see if the user has entered a capital or lower case a
    op_1 = input('Ok, will that be conventional, the special or Synthetic?\t'
                 '\nA) Conventional'
                 '\nB) Synthetic'
                 '\nC) Special'
                 '\nD) Coolant Flush and Refill')
    if op_1 == 'A' or op_1 == 'a':
        oil_1 = int(input('Okay, looks like you\'ve selected a conventional oil change. Please press enter to confirm '
                          '\nyou are aware of the price: '))
    if op_1 == 'B' or op_1 == 'd':
        oil_1 = int(input('Okay, looks like you\'ve selected a synthetic oil change. Please press enter to confirm '
                          '\nyou are aware of the price: '))
    if op_1 == 'C' or op_1 == 'c':
        oil_1 = int(input('Okay, looks like you\'ve selected a special oil change. Please press enter to confirm '
                          '\nyou are aware of the price: '))
