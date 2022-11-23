testcode = ['''
func main void
  var object x
  assign x.member1 42
  assign x.member2 "blah"	 
  funccall foo x
endfunc

func foo q:object void
  funccall print q.member1
  assign q.member2 “bletch”  # mutates original x.member2 variable
endfunc








    ''' 
]