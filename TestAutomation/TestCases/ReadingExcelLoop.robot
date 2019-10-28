*** Settings ***
Library   SeleniumLibrary
Resource  ../Resources/UserKeywords.robot


*** Variables ***
${var1}   http://www.thetestingworld.com


*** Test Cases ***
TC_001 Login Logout Functionality
    open browser  ${var1}  Chrome
    maximize browser window
    click element  xpath://a[text()='Login']
    ${row}=  Read Number Of Rows  GeeSlimmy

    : FOR  ${i}  IN RANGE  1  ${row}+1
    \   ${username}=  Read Excel Data Cell  GeeSlimmy  ${i}   1
    \   ${password}=  Read Excel Data Cell  GeeSlimmy  ${i}   2
    \   input text  id:username  ${username}
    \   input text  id:password  ${password}
    \   click button  xpath://button[@type='submit']
    \   sleep  5s

#    log to console  ${row}
#    ${data}  Read Excel Data Cell  GeeSlimmy  1  1
#    log to console  ${data}
#
#
#
#    click element  xpath://button[@type='submit']
#    sleep  5s
