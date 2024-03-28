import streamlit as st

def render_navbar():
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
    st.markdown("""
    <head>
    <!-- Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #D91E18; height:80px; margin-top: 40px; margin-bottom: 20px;">
        <div class="container-fluid">
            <img src= "https://i.im.ge/2024/02/25/gcZbVp.Screenshot-2024-02-25-at-4-06-59-PM.png" alt="Logo" style="height: 75px; width: auto; margin-right: 5px; margin-top: 10px; margin-bottom: 5px">
            <div class="navbar-collapse justify-content-end">
                <ul class="navbar-nav">
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownAbout" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="color: white;">
                            ℹ About
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdownAbout">
                            <a class="dropdown-item" href="#">Our Team</a>
                            <a class="dropdown-item" href="#">Mission</a>
                            <div class="dropdown-divider"></div>
                            <a class="dropdown-item" href="#">Company Info</a>
                        </div>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownContact" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="color: white;">
                            👤 Contact
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdownContact">
                            <a class="dropdown-item" href="mailto:rkushwaha@sigmoidanalytics.com">Email: rkushwaha@sigmoidanalytics.com</a>
                            <a class="dropdown-item" href="#">Phone</a>
                            <div class="dropdown-divider"></div>
                            <a class="dropdown-item" href="#">Location</a>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    """, unsafe_allow_html=True)


