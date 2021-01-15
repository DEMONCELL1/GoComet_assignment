import react, { Component} from 'react';
import Api from './Api.js';
 import './App.css';
 import PostInfo from './search.js';


class App extends Component {
  render() {

    return (

      <div className="pager">
       <h2>Search a Topic</h2>
       <form className="form-search">
        <div className="input-append">
          <input type="text" placeholder="Search" className="search-query"/>
          <button type="button" className="btn"><i className="icon-search"></i></button>
        </div>
       </form>
       <div className="container">
       <h3>Trending</h3>
       <PostInfo />
       <PostInfo />
       <PostInfo />
       <PostInfo />
       </div>
      </div>
    );
  }
}

export default App;
