def fileexchange():
    fileone = str (input("Enter file one name"))
    filetwo = str (input("Enter file two name"))

    fileoneopened = open(fileone,"r+")
    filetwoopened = open(filetwo,"r+")
    
    dataa = fileoneopened.read()
    datab = filetwoopened.read()

    filetwoopened.write(dataa)
    fileoneopened.write(datab)


fileexchange()
