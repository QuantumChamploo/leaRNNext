import wikipedia

frst = wikipedia.page('First generation of video game consoles')
scnd = wikipedia.page('Second generation of video game consoles')
thrd = wikipedia.page('Third generation of video game consoles')
frth = wikipedia.page('Fourth generation of video game consoles')
ffth = wikipedia.page('Fifth generation of video game consoles')
sxth = wikipedia.page('Sixth generation of video game consoles')

total = frst.content + scnd.content + thrd.content + frth.content + ffth.content + sxth.content

make_txt = open("gen_test_entry.txt","w+")
make_txt.write(total)

print (total)