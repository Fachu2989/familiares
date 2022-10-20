# familiares
 
</head>
<body>
    <header>
        <h1 class="Titulo">
            Familiares
        </h1>
    </header>
    <ul>
        
        {% for family in familiares %}
            <li>{{family.nombre}} - {{family.edad}} - {{family.nacimiento}}</li>

        {% endfor %}
            
    </ul>  
</body>
</html>