# This is a sample Python script.
import tabula
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def read_PDF(file):
    # Use a breakpoint in the code line below to debug your script.
    file1 = file
    table = tabula.read_pdf(file1,pages=[1,2])
    view1 = table[0]
    #view2 = table[1]
    print(view1)
    #print(view2)
    view1.to_excel("/Users/alex/Downloads/VT_table.xlsx")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_PDF("https://cs.vt.edu/content/dam/website_cs_vt_edu/checksheets/Computer%20Science%20Major%20Checksheet%202022-2023.pdf")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
