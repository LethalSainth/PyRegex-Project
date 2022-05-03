This program attempts to match lines of input against a list of regular expressions,
for each line the name of the first matching pattern is printed, 
or unknown if no matching pattern is matched.

When run without any arguments, line will be read from standard input.
If given a filename, lines will be read from that file.

Source: http://csweb.wooster.edu/nsommer/cs220/python-regular-expressions.html

N.B: Since I am writing this from Nigeria, I wrote the regular expressions for 
Nigerian Phone numbers instead of the provided American numbers. So it recognizes
the following Nigerian phone no formats: 07012345678, 08012345678, 09012345678,
08112345678, 09112345678, 2347012345678, +2348012345678, 2349112345678 etc.
