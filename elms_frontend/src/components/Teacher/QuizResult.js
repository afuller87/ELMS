// import {Link} from 'react-router-dom';
// import TeacherSidebar from './TeacherSidebar';
import {useState, useEffect} from 'react';
// import {useParams} from 'react-router-dom';
import axios from 'axios';
const baseUrl='http://127.0.0.1:8000/api';
function QuizResult(props){
    const [resultData,setresultData]=useState([]);
    // Fetch courses when page load
    useEffect(()=>{
        try{
            axios.get(`${baseUrl}/fetch-quiz-result/${props.quiz}/${props.student}`)
            .then((res)=>{
                setresultData(res.data);
            });
        }catch(error){
            console.log(error);
        }

    },);

    return (
        
            <div className="modal-dialog">
            <div className="modal-content">
                <div className="modal-header">
                <h5 className="modal-title" id="exampleModalLabel">Quiz Result</h5>
                <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div className="modal-body">
                <table className="table">
                    <tr>
                        <td>Total Questions</td>
                        <td>{resultData.total_questions}</td>
                    </tr>
                    <tr>
                        <td>Attempted Questions</td>
                        <td>{resultData.total_attempted_questions}</td>
                    </tr>
                    <tr>
                        <td>Correct Answered</td>
                        <td>{resultData.total_correct_questions}</td>
                    </tr>
                </table>
                </div>
            </div>
            </div>
        
    );
}

export default QuizResult;