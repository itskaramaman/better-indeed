from django.shortcuts import render


def home(request):
    job_list = [{
        "title": "Senior Engineering - Software Engineer",
        "company": "Capgemini",
        "location": "Vancouver, BC",
        "type": "Full Time",
        "description": "World leader in engineering and R&D services, Capgemini Engineering  the physical and digital worlds. Coupled with the capabilities of the rest of the Group, it helps clients to accelerate their journey towards Intelligent Industry. Capgemini Engineering has more than 55,000 engineer and scientist team members in over 30 countries across sectors including Aeronautics, Space, Defense, Naval, Automotive, Rail, Infrastructure & Transportation, Energy, Utilities & Chemicals, Life Sciences, Communications, Semiconductor & Electronics, Industrial & Consumer, Software & Internet.",
        "created_at": "14-08-2023"
    },
    {
        "title": "Senior Engineering - Software Engineer",
        "company": "Capgemini",
        "location": "Vancouver, BC",
        "type": "Full Time",
        "description": "World leader in engineering and R&D services, Capgemini Engineering  the physical and digital worlds. Coupled with the capabilities of the rest of the Group, it helps clients to accelerate their journey towards Intelligent Industry. Capgemini Engineering has more than 55,000 engineer and scientist team members in over 30 countries across sectors including Aeronautics, Space, Defense, Naval, Automotive, Rail, Infrastructure & Transportation, Energy, Utilities & Chemicals, Life Sciences, Communications, Semiconductor & Electronics, Industrial & Consumer, Software & Internet.",
        "created_at": "14-08-2023"
    }]

    job = {
        "title": "Senior Engineering - Software Engineer",
        "company": "Capgemini",
        "location": "Vancouver, BC",
        "type": "Full Time",
        "description": "World leader in engineering and R&D services, Capgemini Engineering  the physical and digital worlds. Coupled with the capabilities of the rest of the Group, it helps clients to accelerate their journey towards Intelligent Industry. Capgemini Engineering has more than 55,000 engineer and scientist team members in over 30 countries across sectors including Aeronautics, Space, Defense, Naval, Automotive, Rail, Infrastructure & Transportation, Energy, Utilities & Chemicals, Life Sciences, Communications, Semiconductor & Electronics, Industrial & Consumer, Software & Internet.",
        "created_at": "14-08-2023"
    }

    return render(request, 'main/home.html',
                  {'job_list': job_list, 'job': job})
