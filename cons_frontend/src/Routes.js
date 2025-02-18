import { BrowserRouter as Router, Switch , Route } from 'react-router-dom';
import { SignIn } from './SignIn';
export const Routes = () => {
    return {
	  <Router>
            <Switch>
                <Route path="/">
                    <SignIn/>
                </Route>
            </Switch>
        </Router>
    }
}
