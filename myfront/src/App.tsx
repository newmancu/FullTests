import React from 'react';
import './sass/_app.sass'


const getCookies = (url: string) => {
  const xhr = new XMLHttpRequest()
  xhr.open('GET', url, true)
  xhr.withCredentials = true
  xhr.send()
  xhr.onload = (ev) => {
    const data = xhr.response
    console.log(data)
  }
}

const tryRequest = () => {
  getCookies("http://127.0.0.1:8000/cookies/get/")
}

function App() {
  return (
    <div className="App">
      <h2 className="app-title">
        Hello, World!
      </h2>
      <button onClick={tryRequest}>COOKIES!!!</button>
    </div>
  );
}

export default App;
