This is unrelated to both johnny.decimal and the Dewey Decimal System

D.E.W.E.Y. is the file structure that i've invented to organize my computers. It revolves around three main ideas:
  1. Give each file a unique, standard identifier
  2. Each folder and subfolder uses place value to signify prescision
  3. Use a standard formatting style for automation and non-user action

### General Overview

The file structure has five divisions.
- root `000-900`
- first `010-090`
- second `011-019`
- third `011.1-011.9`
- fourth, or file `011.101-011.199`


The root folder is seperated into maximum 10 categories,`000-900`.

Each of those ten categories will have ten subfolders, `210-290`
and each of those ten categories will have ten subfolders, `211-219`
and then one more set of ten down, so `214.1-214.9`

In theory, this pattern could be continued infintely, or started from a higher point, from the thousands or ten thousands if the user needed more subfolders.



In the maximum amount of subfolders, `(###.#)` each file is given an ID out of 100, for example
`214.934` or `567.433`
This lets you have a large amount of files. If a file is not in the fourth division of a subfolder, it is given an ID of whatever the subfolder would be. 
If a file is in the subfolder `340`, it would be given an ID between `341` and `349`, depending on how many files are in the folder.

Additionally, each folder and file is given a title, so `300 School` or `651.324 orange-logo-zip.jpg`
Here's an example of a folder structure.
```
100 Notes
	110 Class Notes
	120 Lecture Notes
		121 Precalc Notes
		122 Chem Notes
			122.1 Module 1 Notes
			122.2 Module 2 Notes
			122.3 Module 3 Notes
				122.301 mod-3-notes.docx
	130 Personal Notes
```
As you can see, each subfolder is given a new level of identification via place value. This is the main concept of D.E.W.E.Y.

Let's dive deeper into the three main sections of D.E.W.E.Y.


### 1. Give each file a unique, standard identifier
The goal of point one was to easily be able to write down a location of a file for later, and it easily be returned to without having to remember the name, ID, or other elements of a file. The optimal placement for a file is in the third division, so that it can recieve a FileID of 6 digits. However, it can be difficult to specify a category beyond a certain value, imagine trying to have a fourth division for the second division of Typography or Fonts.
This system lets files use FolderIDs to remove extraneous folders. However, the one downside of this method is that it limits the number of files you can have to nine without creating another subfolder.

### 2. Each folder and subfolder uses place value to signify prescision
As described previously, the higher division you are in, the less zeroes there will be in the ID. That way you can accurately get a picture of what division a subfolder is in based on its ID alone. This method also allows for infinite expansion, by both increasing the starting value, or increasing the number of digits after the decimal place. Another advantage of using place value is ease of automation, see #3.

### 3. Use a standard formatting style for automation and non-user action
The standard formatting style allows scripts like Python, Shortcuts, Automator, and more to automatically label, move, or ID folders. It also allows for a quickly searchable interface. I've included autolabel.py, which given a file path, will rename the file path based on its file structure. (Using the five main divisions) The code is bad. Its probably the worst way to do it. but it works, and that's what matters.

In sum, this whole file system is probably unnecessary. However, you get to have your own little database, just for you.

the end
