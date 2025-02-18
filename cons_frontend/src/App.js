import { BrowserRouter as Router, Routes , Route } from 'react-router-dom';
import SignIn from './SignIn';
//import { Routes } from './Routes';
import './App.css';

export const App = () =>  {
  return (
        <Router>
            <Routes>
                <Route path="/">
                    <SignIn/>
                </Route>
            </Routes>
        </Router>
       // document.getElementById("root");
  );
}


