""" Miguel Rivas Méndez
    migueladanrm@outlook.com
    << Log list formatting tool >>
"""

def getFormattedLog(headers, content):
    if(len(headers) == len(content[0])):
        output = ""
        max_size = []

        # obtención de tamaño máximo
        for x in range(len(headers)):
            val = len(headers[x])
            for item in content:
                if len(item[x]) > val:
                    val = len(item[x])
            max_size.append(val)

        # creación de las etiquetas de los headers.
        for x in range(len(headers)):
            tmp_lbl = headers[x]
            while len(tmp_lbl) < max_size[x]:
                tmp_lbl += " "
            tmp_lbl += " "
            output += tmp_lbl

        output += "\n"

        #agregación de barras de división
        for x in range(len(headers)):
            tmp = ""
            while len(tmp) < max_size[x]:
                tmp += "="
            tmp += " "
            output += tmp

        output += "\n"

        # adición de datos de la lista
        for element in content:
            tmp = ""
            for si_indx in range(len(element)):
                list_part = element[si_indx]
                while len(list_part) < max_size[si_indx]:
                    list_part += " "
                list_part += " "
                tmp += list_part
            tmp += "\n"
            output += tmp
        output += "\n"

        return output
    else:
        return None