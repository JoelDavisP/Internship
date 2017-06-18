def rotx(st,num):
 if(num>0):
  print st
  print num
  for a in st:
   sn = ord(a)
   nsn = sn + num
   if nsn > 122:
    sn = sn - 26
    nsn = sn +num
   elif nsn >= 97 and nsn <= 122:
    sn = sn - 26
    nsn = sn + num
   a = chr(nsn)
   print a
 elif(num<0):
    print st,num
    for a in st:
        sn = ord(a)
        nsn = sn + num
        if nsn < 97:
            sn = sn + 26
            nsn = sn +num
        if nsn >= 97 and nsn <= 122:
            a = chr(nsn)
        print a 

rotx('meeeelon',-10) 
