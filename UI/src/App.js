import React, { Component } from 'react';
//import logo from './logo.svg';
//import './App.css';
import axios from 'axios';




class App extends React.Component {


  state = {
    listOfImages : {"chicken" : require("./images/chicken.png")},
    listOfNames : ["chicken"],
    statusData : {"status":"test", "display":"test1"}
  };

  componentDidMount(){

    setInterval( () => {
      axios.get(`http://192.168.43.69:8080/Data`).then(res => {
        console.log(res);
        this.setState({statusData : res.data});
        //console.log(typeof (this.state.statusData["display"]))
        //console.log(typeof (this.state.listOfNames[0]))
      }).catch(function(res) {
        if(res instanceof Error) {
          console.log(res.message);
        } else {
          console.log(res.data);
        }
      })
    },500);

  };


  render(){

    //var imageName = require(this.state.listOfImages["chicken"]);
    // this.state.statusData["display"] === this.state.listOfNames[0]
    if(false){
      //console.log(toString(this.state.statusData["display"]) in this.state.listOfNames)
      return (
        <div style={{ position: "static", backgroundColor: this.state.statusData["status"], padding:"5%", height: "99%", width: "99%"}}>
          <div style={{position: "static", textAlign: "center", marginBottom: "15%", marginTop: "10%", padding:"10%", marginLeft: "15%", width:"40%", height:"30%",backgroundColor: "white"}}>
            <img style={{width:"60%", height:"60"}} src={this.state.listOfImages["chicken"]} />
          </div>
        </div>
      );
    }else{
      //console.log(this.state.listOfNames)
      //console.log(toString(this.state.statusData["display"]) in this.state.listOfNames)
      return (
        <div style={{ position: "static", backgroundColor: this.state.statusData["status"], padding:"5%", height: "99%", width: "99%"}}>
          <div style={{ fontStyle: "italic", fontSize:"30px", textAlign: "center", marginBottom: "15%", marginTop: "10%", padding:"5%", marginLeft: "5%",  width:"65%", backgroundColor: "white"}}>
            <h1 style={{display : this.state.statusData["display"] === this.state.listOfNames[0] ? 'none' : ""}} className = "centered whiteFont">
            {this.state.statusData["display"]}
            </h1>
            <img style={{display : this.state.statusData["display"] === this.state.listOfNames[0] ? '' : "none", width:"30%", height:"30"}} src={this.state.listOfImages["chicken"]} />
          </div>
        </div>
      );
    }

    
  }
}

export default App;
