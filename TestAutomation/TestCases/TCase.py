# from Library.CommonModule import A
# # Using 'from' we need to say what class we are importing
# objA= A()
# objA.startbrowser()

import Pages.Login.ABC

obj = Pages.Login.ABC.C()
obj.mytesting()

from Pages.Login.ABC import C

obj= C()
obj.mytesting()

# import Library.CommonModule
#
# objA = Library.CommonModule.A()
# objA.startbrowser()
#
# objB = Library.CommonModule.B()
# objB.startbrowser()