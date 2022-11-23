testcode = ['''
func main void  
  var object x
  assign x.a 10 				# x.a’s type is int
  var int y
  assign y 20

  assign y * x.a y
  funccall print y			# prints 200
endfunc











    ''' 
]