
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    # print(words_count(file_contents))
    # print(char_count(file_contents))
    print("--- Begin report of books/frankenstein.txt ---")
    
    print(f"{words_count(file_contents)} words found in the document")
    report(char_count(file_contents))
    print("--- End report ---")

def words_count(s):
    return len(s.split())

def char_count(s):
    l = s.lower()
    dik = {}
    for i in range(len(l)):
        if l[i] in dik:
            dik[l[i]] += 1
        else: dik[l[i]] = 1
    return dik

def sort_on(dict):
    return dict["num"]

def report(dik):
    list_dict = []
    for i in dik:
        if i.isalpha():
            list_dict.append({"name":i, "num":dik[i]})

    
    list_dict.sort(reverse=True, key=sort_on)
    
    for i in list_dict:
        print(f"The '{i["name"]}' character was found {i["num"]} times")   

main()
