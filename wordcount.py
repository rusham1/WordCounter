def countWords():
    print("\nEnter a text to count the words: (Enter twice to end.)")
    count=0
    lines=[]
    while True:
        line=str(input())
        if line=="":
            break
        for _ in range(len(line)):
            if line[_] in (" "):
                count+=1
        lines.append(line)
        count+=1
    text="\n".join(lines)
    count-=1
    return count

def main():
    wordCount=countWords()
    print(f"The number of words in the text: {wordCount}")

if __name__=="__main__":
    main()