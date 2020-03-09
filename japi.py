import urllib.request

def getStockData(inputSym):
    nasdaqSym = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + str(inputSym) + "&apikey=ZYJMMIKD9Z5EMI8H"
    try:
        connection = urllib.request.urlopen(nasdaqSym)
        responseStr = connection.read().decode()
    except:
        return notFound()
    #If the symbol isn't found
    if("Error" in responseStr):
        return notFound()
    foo = responseStr.split('\n')
    return foo[13][25:33] #close price of today   

def notFound():
    return "NAN"

def main():
    logFile = open("japiLog.txt", "w")
    while(True):
        #ask for symbol
        inputSym = input("Enter a stock symbol (or quit) ")
        print("Enter a stock symbol (or quit)", file=logFile)
        print("Input: " + inputSym, file=logFile)

        #Quitting check
        if(inputSym == "quit"):
            break
        #Check price of stock
        price = getStockData(inputSym)
        
        #Error check
        if(price == "NAN"):
            print("The stock with Symbol '" + inputSym + "' could not be found.")
            print("The stock with Symbol '" + inputSym + "' could not be found.", file=logFile)

        else:
            print("The current price of " + inputSym + " is: " + price)
            print("The current price of " + inputSym + " is: " + price, file=logFile)

        #Newline for appearance
        print()
        print("", file=logFile)
        
    print("Stock Quotes retrieved successfully!")
    print("Thanks, bye!", file=logFile) 
    logFile.close()

main()