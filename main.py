def E(number_string):
    def strtolist(value):
        i = 0
        list = []
        while i < len(str(value)):
            list.append(value[i])
            i = i + 1
        return list
    def listtostr(list):
        string = ''
        i = 0
        while i < len(list):
            string = string + list[i]
            i = i + 1
        return string
    try:
        split = (number_string.split(sep="e"))
        number = str(split[0])

        try:
            spliter = str(split[1]).split("-")
            power = spliter[1]
            mins = (strtolist(number))
            mins.remove(".")
            for i in range(0, int(power)):
                mins.insert(0, "0")
            mins.insert(1, ".")
            return listtostr(mins)

        except:
            plus = str(split[1]).split("+")
            power = plus[1]
            plus_number = float(number) * float(power)
            return plus_number

    except:
        return number_string

