import csv
import xml.etree.cElementTree as ET

tree = ET.parse("CEP.xml")
root = tree.getroot()

xml_data_to_csv = open("cep.csv", "w")
list_head = []

csv_writer = csv.writer(xml_data_to_csv)
count = 0
for element in root.findall("cep"):
    list_nodes = []

    if count == 0:
        cep = element.find("cep").tag
        list_head.append(cep)
        logradouro = element.find("logradouro").tag
        list_head.append(logradouro)
        complemento = element.find("complemento").tag
        list_head.append(complemento)
        bairro = element.find("bairro").tag
        list_head.append(bairro)
        localidade = element.find("localidade").tag
        list_head.append(localidade)
        uf = element.find("uf").tag
        list_head.append(uf)
        ibge = element.find("ibge").tag
        list_head.append(ibge)
        gia = element.find("gia").tag
        list_head.append(gia)
        ddd = element.find("ddd").tag
        list_head.append(ddd)
        siafi = element.find("siafi").tag
        list_head.append(siafi)
        csv_writer.writerow(list_head)
        count = count + 1


    cep = element.find("cep").text
    list_nodes.append(cep)

    logradouro = element.find("logradouro").text
    list_nodes.append(logradouro)

    complemento = element.find("complemento").text
    list_nodes.append(complemento)

    bairro = element.find("bairro").text
    list_nodes.append(bairro)

    localidade = element.find("localidade").text
    list_nodes.append(localidade)

    uf = element.find("uf").text
    list_nodes.append(uf)

    ibge = element.find("ibge").text
    list_nodes.append(ibge)

    gia = element.find("gia").text
    list_nodes.append(gia)

    ddd = element.find("ddd").text
    list_nodes.append(ddd)

    siafi = element.find("siafi").text
    list_nodes.append(siafi)

    csv_writer.writerow(list_nodes)

xml_data_to_csv.close()