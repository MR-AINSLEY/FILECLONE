package main

import "fmt"

type Person struct {
  name string
  username string
  age int
  hobbies []string
  job string
}

func main() {
  var me = new(Person)
  
  me.name     = "Limon-Hossain"
  me.username = "LMNx9-JOHNY"
  me.age      = "18"
  me.job      = "Python Developer | Data Scienctist"
  me.hobbies  = []string{"code", "anime", "music"," guiterist"," gaming"}
  
  fmt.Println(me)
}
