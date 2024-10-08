from flask import render_template_string
from flask_security import auth_required, current_user, roles_required

def create_view(app):
    # homepage
    
    @app.route("/")
    def home():
        return render_template_string(
            """
                <h1> This is homepage </h1>
                <div>
                <a href="/login">login</a>
                </div>
                <a href="/profile"> Profile page </a>
            """
            
        )
        
    @app.route('/profile')
    @auth_required('session','token')
    def profile():
        return render_template_string(
            """
            <h1>This is profile page </h1>
            <p> Welcome {{current_user.email}}
            <a href="/logout">logout</a>
            
            """
            
        )
        
    @app.route('/inst-dashboard')
    @roles_required('instructor')
    def inst_dashboard():
        return render_template_string(
            """
                <h1> Instructor profile </h1>
                <p> It should be only visible to instructor </p>
            """
            
        )
        
    @app.route('/admin')
    @roles_required("admin")
    def admin_dashboard():
        return render_template_string(
            """
            
            <h1> Admin Dashboard </h1>
            """
            
        )