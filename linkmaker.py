import hashlib
#creates the strings for the subreddit
reddit = "https://www.reddit.com/r/"
subreddit = input("Enter the subreddit: ")
subreddit = subreddit + "/"
#opens the files, file1 is the input, file2 is the output
file1 = open("input.txt", "r")
file2 = open("output.txt", "w")
x = 1
for modify in file1.readlines():

    #reads line in from the file, naming it modify
    #modify = (file1.readlines()[x])


    #deletes everything up to the post ID
    mod_string = modify[33:]
    mod_string = mod_string[:-2]#this just takes off the quotation mark
    throwaway, mod_string = mod_string.split("\\")
    #removes duplatic strings
    mod_string = mod_string.replace("_11","")
    mod_string = mod_string.replace("_10","")
    mod_string = mod_string.replace("_9","")
    mod_string = mod_string.replace("_8","")
    mod_string = mod_string.replace("_7","")
    mod_string = mod_string.replace("_6","")
    mod_string = mod_string.replace("_5","")
    mod_string = mod_string.replace("_4","")
    mod_string = mod_string.replace("_3","")
    mod_string = mod_string.replace("_2","")
    mod_string = mod_string.replace("_1","")

    #splits the post ID from the title
    part1, part2 = mod_string.split("_")

    #removes file extensions from url
    part2 = part2.replace(".mp4","")
    part2 = part2.replace(".gif","")
    part2 = part2.replace(".png","")
    part2 = part2.replace(".jpeg","")
    part2 = part2.replace(".jpg","")
    part2 = part2.replace(".txt","")
    #removes characters
    part2 = part2.replace("!","")
    part2 = part2.replace("@","")
    part2 = part2.replace("#","")
    part2 = part2.replace("$","")
    part2 = part2.replace("%","")
    part2 = part2.replace("^","")
    part2 = part2.replace("&","")
    part2 = part2.replace("*","")
    part2 = part2.replace("(","")
    part2 = part2.replace(")","")
    part2 = part2.replace("-","")
    part2 = part2.replace("_","")
    #need to delete the _1 _2 _3 ones here
    part2 = part2.replace("+","")
    part2 = part2.replace("=","")
    part2 = part2.replace("[","")
    part2 = part2.replace("]","")
    part2 = part2.replace("{","")
    part2 = part2.replace("}","")
    part2 = part2.replace("|","")
    part2 = part2.replace(";","")
    part2 = part2.replace("'","")
    #part2 = part2.replace(" ","") cant figure out how to remove quotes
    part2 = part2.replace(",","")
    part2 = part2.replace("<","")
    part2 = part2.replace(">","")
    part2 = part2.replace(".","")
    part2 = part2.replace("?","")
    part2 = part2.replace("/","")
    #replace _ with space
    part2 = part2.replace(" ","_")

    #makes the file subreddit string
    str = reddit + subreddit + "comments/" + part1 + "/" + part2
    #writes file to output
    file2.write(str)
    file2.write("\n")
    x += 1
    print(str)
        
else:
#closes file
    file1.close()
