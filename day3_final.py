print('''
                    ____
                 _.' :  `._
             .-.'`.  ;   .'`.-.
    __      / : ___\ ;  /___ ; \      __
  ,'_ ""--.:__;".-.";: :".-.":__;.--"" _`,
  :' `.t""--.. '<@.`;_  ',@>` ..--""j.' `;
       `:-.._J '-.-'L__ `-- ' L_..-;'
         "-.__ ;  .-"  "-.  : __.-"
             L ' /.------.\ ' J
              "-.   "--"   .-"
             __.l"-:_JL_;-";.__
          .-j/'.;  ;""""  / .'\"-.
        .' /:`. "-.:     .-" .';  `.
     .-"  / ;  "-. "-..-" .-"  :    "-.
  .+"-.  : :      "-.__.-"      ;-._   \
  ; \  `.; ;                    : : "+. ;
  :  ;   ; ;                    : ;  : \:
 : `."-; ;  ;                  :  ;   ,/;
  ;    -: ;  :                ;  : .-"'  :
  :\     \  : ;             : \.-"      :
   ;`.    \  ; :            ;.'_..--  / ;
   :  "-.  "-:  ;          :/."      .'  :
     \       .-`.\        /t-""  ":-+.   :
      `.  .-"    `l    __/ /`. :  ; ; \  ;
        \   .-" .-"-.-"  .' .'j \  /   ;/
         \ / .-"   /.     .'.' ;_:'    ;
          :-""-.`./-.'     /    `.___.'
                \ `t  ._  /  bug :F_P:
                 "-.t-._:'
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the Yoda.")

path = input("Choose a path: Left or Right ")
if path == 'Left' or path == 'left':
    sinkOrSwim = input('Would you like to swim or wait? ')
    if sinkOrSwim == 'wait' or sinkOrSwim == 'Wait':
        door = input('Pick a door: Red, Blue, or Yellow: ')
        if door == "yellow" or door == "Yellow":
            print('You found the wisest of them all!')
        else:
            print('You fell into a dark realm. Game Over.')
    else:
        print('Captured by Storm Troopers. Game Over.')
else:
    print('You got ejected into space. Game Over.')
