# No Imports
# Read through 'mbox-short.txt'
# Create a python dictionary that maps the sender's mail adress to the number of times they appear
# Read dictionary to determine who sent the most messages
# Must use .get() and .items()
# Hint: for k:v in [dict name].items()
# (k =  key (the email adresses))
# (v = value (count))
# i.e, 'Brand':'Ford'
# NO LISTS

print('Scanning mbox-short.txt...')
print('Done!')
print('')
print('Posts:')

emaildict = {}                                                                             
numindex = 0                                                                               
emailstr = ''

# epath = 'D:/mbox-short.txt'                                                               # USB path / Home path
epath = 'I:/Testing/mbox-short.txt'                                                         # School path
emailscript = open(epath, 'r')                                                              # Opens path to mbox-short.txt for reading
emailscript = emailscript.read()                                                            # Reads lines

numindex = emailscript.find("From")

while numindex < len(emailscript):                                                          # Main while loop that allows me to scan the whole script
    numindex = emailscript.find("From", numindex)                                           # Searches for the word 'From'
    if numindex == -1:                                                                      # End condition (returning -1 means it's reached the end of the script)
        break
    numindex = numindex + 1                                                                 # Numindex is the place in the string that i'm currently on

    if (emailscript[numindex + 3] == ' '):                                                  # Jumps forward a few characters after the 'From' to check for a space (Colon Clause)
        numindex = numindex + 4                                                             # Jumps to first character of the email
        spacedetected = False                                                               # Sets up for email while loop
        
        while spacedetected == False:                                                       # Parses emails character by character until there's a space
            if (emailscript[numindex] != ' '):                                              # Checks for a space
                emailstr = emailstr + emailscript[numindex]                                 # Adds each character to a seperate string individually
                numindex = numindex + 1                                                     # Increments by 1 each time
            else:                                                                           # Checks if a space is found
                spacedetected = True                                                        # Break the while loop
                if emailstr in emaildict:                                                   # Checks if the email is already in the dictionary
                    emaildict[emailstr] += 1                                                # Adds one to the value of the email
                    emailstr = ''                                                           # Wiping the string for next entry

                else:                                                                       # If the email is a new entry in the dictionary
                    emaildict[emailstr] = 1                                                 # Adds the email to the dictionary with a value of 1
                    emailstr = ''                                                           

    else:
         pass

biggestposter = max(emaildict, key=emaildict.get)                                           # Gets email of the person with the most posts (Key)
mostposts = max(emaildict.values())                                                         # Gets the highest number of posts (Value)

print(emaildict)                                                                            # Prints dictionary with all the emails in it
print('')
print(f'The person with the most posts on this site is {biggestposter} with {mostposts} posts!')
print('')

input('-Press Enter to Exit-')                                                              # Prevents the program from closing prematurely

