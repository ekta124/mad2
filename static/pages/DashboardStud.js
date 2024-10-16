import StudyResource from '../components/StudyResource.js'

const DashboardStud = {
    template:`
        <div>
        <h1> This is student dashboard</h1>
            <div v-for="resource in allResource">
                <StudyResource :topic="resource.topic" :content="resource.content" creator="me"/>
            </div>
        </div>
    `,
    data() {
        return{
            allResource: []
        };
    },
    async mounted() {
        const res = await fetch(window.location.origin + "/api/resources",{
            headers:{
                "Authentication-token": sessionStorage.getItem('token'),
            },
        });
        try{
            const data = await res.json();
            console.log(data);
            this.allResource = data;
        } catch(e){
            console.log("error in converting to json")
        }
        
    },
    components: {StudyResource},
};


export default DashboardStud