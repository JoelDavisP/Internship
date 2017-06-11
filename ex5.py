def count(test, cnt_ltr):
 x = len(test)
 cntr=0
 while x!= 0:
  if test[x-1] == cnt_ltr:
    cntr= cntr + 1
  x= x-1
 print cntr 
count(raw_input(), raw_input())
