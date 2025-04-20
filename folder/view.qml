import QtQuick
  
  
    
    ListView {
      width: 280
      height: 200

      required model
      
      delegate: Rectangle {
        color: "lightgray"
        height: 25
        width: 280

        Row {
          spacing: 0

          Text  { //  Name
            height: 25
            width: 50
            text: modelData[0]
          }
          Text  { //  Surname
            height: 25
            width: 50
            text: modelData[1]
          }
          Text  { //  Number 
            height: 25
            width: 40
            text: modelData[2]
          }
          Text  { //  City 
            height: 25
            width: 40
            text: modelData[3]
          }
          Text  { //  Street 
            height: 25
            width: 100
            text: modelData[4]
          }
        }
      }
    }
