import {useParams} from 'react-router-dom';
import {useState, useEffect} from 'react';
import axios from 'axios';
const baseUrl='http://127.0.0.1:8000/api';
function Page(){
    const [pageData,setpageData]=useState([]);
    let {page_id,page_slug}=useParams();
    // Fetch courses when the page loads
    useEffect(()=>{
        try{
            axios.get(baseUrl+'/pages/'+page_id+'/'+page_slug)
            .then((res)=>{
                setpageData(res.data);
            });
        }catch(error){
            console.log(error);
        }
    },[page_id]);
    return (
        <div className="container mt-4">
            <h2>{pageData.title}</h2>
            <p>{pageData.content}</p>
        </div>
    )
}

export default Page;