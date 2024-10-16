import StudyResource from '../components/StudyResource.js'

const DashboardInst = {
    template:`
        <div>
        <h1> This is Instructor dashboard</h1>
        <h2> New Resources </h2>
            <div v-for="res in newResource">
                <StudyResource :topic="res.topic" :content="res.content" creator="me" :approvalRequired='true' :approvalID ="res.id"/>
        <h2>Approved Resources </h2>
            <div v-for="resource in allResource">
                <StudyResource :topic="resource.topic" :content="resource.content" creator="me"/>
            </div>
        </div>
    `,
    data() {
        return{
            allResource: [],
            newResource: []
        };
    },
    async mounted() {
        const res = await fetch(window.location.origin + "/api/resources",{
            headers: {
                "Authentication-Token": sessionStorage.getItem('token'),
            },
        });
        try {
            const data = await res.json();
            this.allResource = data;
        } catch(e){
            console.log("error in converting to json")
        }
        const resNew = await fetch(window.location.origin + "/api/resources/unapproved",{
            headers:{
                "Authentication-token": sessionStorage.getItem('token'),
            },
        });
        try{
            const data = await resNew.json();
            this.newResource = data;
        } catch(e){
            console.log("error in converting to json")
        }


        
    },
    components: {StudyResource},
};


export default DashboardInst