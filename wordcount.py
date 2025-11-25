import string

def countWords():
    words=[]
    print("\nEnter a text to count the words: (Enter twice to end.)")
    count=0
    lines=[]
    while True:
        line=str(input())
        if line=="":
            break
        lines.append(line)
    text="\n".join(lines)

    for p in string.punctuation:
        text=text.replace(p," ")
    wordsList=text.split() 
    
    wordDict={}
    for w in wordsList:
        wLower=w.lower()
        if wLower in wordDict:
            wordDict[wLower]+=1
        else:
            wordDict[wLower]=1
    dictWordsCount=[]
    for w,c in wordDict.items():
        dictWordsCount.append({
            "wordName":w,
            "wordCount":c
        })
    

    print(f"{'Word':<15} {'Frequency':<10}")  
    print("-" * 25)  

    for word, count in wordDict.items():
        print(f"{word:<15} {count:<10}")
    return sum(wordDict.values())

def main():
    print("\n================== WORD COUNTER ===================\n")
    wordCount=countWords()
    print(f"\nThe total number of words in the text: {wordCount}\n")

if __name__=="__main__":
    main()