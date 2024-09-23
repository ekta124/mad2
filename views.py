from flask import render_template_string

def create_view(app):
    # homepage
    
    @app.route("/")
    def home():
        return render_template_string(
            """
                <h1> This is homepage </h1>
            """
            
        )