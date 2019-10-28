*** Settings ***
Library  ../TestData/ReadData.py

*** Keywords ***
Read Number Of Rows
    [Arguments]  ${sheetname}
    ${maxr}=  FETCH NUMBER OF ROWS  ${sheetname}
    [Return]  ${maxr}

Read Excel Data Cell
    [Arguments]  ${sheetname}  ${row}  ${cell}
    ${celldata}=  FETCH CELL DATA  ${sheetname}  ${row}  ${cell}
    [Return]  ${celldata}



