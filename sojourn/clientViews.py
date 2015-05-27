import flask

from railz.base import BaseView, Route

class RootView(BaseView):
    
    @Route('/')
    def get(self):
        return flask.render_template('client/root.jinja2', name="World")

SOJOURNS = [
    {
        'id': "the-nyu-area",
        'name': "The NYU Area",
        'location': [40.7304, -74.0001],
        'moments': [
            {
                'id': "1",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/scene1.mp3",
                'destination': {
                    'location': [40.7304, -74.0001],
                    'radius': 50,
                    'next': "2",
                }
            },
            {
                'id': "2",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/scene2.mp3",
                'next': "3",
            },
            {
                'id': "3",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/scene3.mp3",
                'destination': {
                    'location': [40.7310, -73.9995],
                    'radius': 50,
                    'next': "4",
                }
            },
            {
                'id': "4",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/scene4.mp3",
                'next': "5",
            },
            {
                'id': "5",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/scene5.mp3",
                'destination': {
                    'location': [40.7295, -73.9965],
                    'radius': 50,
                    'next': "6",
                }
            },
            {
                'id': "6",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/scene6.mp3",
                'next': "7",
            },
            {
                'id': "7",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/scene7.mp3",
                'destination': {
                    'location': [40.7297, -74.0007],
                    'radius': 50,
                    'next': "8",
                }
            },
            {
                'id': "8",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/scene8.mp3",
                'next': None,
            },
        ]
    },
    {
        'id': "home-2-work",
        'name': "Home 2 Work",
        'location': [40.7351, -74.0017],
        'moments': [
            {
                'id': "1",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/htw1.mp3",
                'destination': {
                    'location': [40.7351, -74.0017],
                    'radius': 50,
                    'next': "2",
                }
            },
            {
                'id': "2",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/htw2.mp3",
                'next': "3",
            },
            {
                'id': "3",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/htw3.mp3",
                'destination': {
                    'location': [40.7353, -74.0003],
                    'radius': 50,
                    'next': "4",
                }
            },
            {
                'id': "4",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/htw4.mp3",
                'next': "5",
            },
            {
                'id': "5",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/htw5.mp3",
                'destination': {
                    'location': [40.7346, -73.9999],
                    'radius': 50,
                    'next': "6",
                }
            },
            {
                'id': "6",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/htw6.mp3",
                'next': "7",
            },
            {
                'id': "7",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/htw7.mp3",
                'destination': {
                    'location': [40.7347, -73.9987],
                    'radius': 50,
                    'next': "8",
                }
            },
            {
                'id': "8",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/htw8.mp3",
                'next': "9",
            },
            {
                'id': "9",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/htw9.mp3",
                'destination': {
                    'location': [40.7341, -73.9971],
                    'radius': 50,
                    'next': "10",
                }
            },
            {
                'id': "10",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/htw10.mp3",
                'next': "11",
            },
            {
                'id': "11",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/htw11.mp3",
                'destination': {
                    'location': [40.7334, -73.9954],
                    'radius': 50,
                    'next': "12",
                }
            },
            {
                'id': "12",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/htw12.mp3",
                'next': "13",
            },
            {
                'id': "13",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/htw13.mp3",
                'destination': {
                    'location': [40.7327, -73.9938],
                    'radius': 50,
                    'next': "14",
                }
            },
            {
                'id': "14",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/htw14.mp3",
                'next': "15",
            },
            {
                'id': "15",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/htw15.mp3",
                'destination': {
                    'location': [40.7333, -73.9933],
                    'radius': 50,
                    'next': "16",
                }
            },
            {
                'id': "16",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/htw16.mp3",
                'next': "17",
            },
            {
                'id': "17",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/htw17.mp3",
                'destination': {
                    'location': [40.7329, -73.9924],
                    'radius': 50,
                    'next': "18",
                }
            },
            {
                'id': "18",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/htw18.mp3",
                'next': None,
            },
        ]
    },
    {
        'id': "work-2-home",
        'name': "Work 2 Home",
        'location': [40.7329, -73.9924],
        'moments': [
            {
                'id': "1",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/wth1.mp3",
                'destination': {
                    'location': [40.7329, -73.9924],
                    'radius': 50,
                    'next': "2",
                }
            },
            {
                'id': "2",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/wth2.mp3",
                'next': "3",
            },
            {
                'id': "3",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/wth3.mp3",
                'destination': {
                    'location': [40.7333, -73.9933],
                    'radius': 50,
                    'next': "4",
                }
            },
            {
                'id': "4",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/wth4.mp3",
                'next': "5",
            },
            {
                'id': "5",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/wth5.mp3",
                'destination': {
                    'location': [40.7327, -73.9938],
                    'radius': 50,
                    'next': "6",
                }
            },
            {
                'id': "6",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/wth6.mp3",
                'next': "7",
            },
            {
                'id': "7",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/wth7.mp3",
                'destination': {
                    'location': [40.7334, -73.9954],
                    'radius': 50,
                    'next': "8",
                }
            },
            {
                'id': "8",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/wth8.mp3",
                'next': "9",
            },
            {
                'id': "9",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/wth9.mp3",
                'destination': {
                    'location': [40.7341, -73.9971],
                    'radius': 50,
                    'next': "10",
                }
            },
            {
                'id': "10",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/wth10.mp3",
                'next': "11",
            },
            {
                'id': "11",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/wth11.mp3",
                'destination': {
                    'location': [40.7347, -73.9987],
                    'radius': 50,
                    'next': "12",
                }
            },
            {
                'id': "12",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/wth12.mp3",
                'next': "13",
            },
            {
                'id': "13",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/wth13.mp3",
                'destination': {
                    'location': [40.7346, -73.9999],
                    'radius': 50,
                    'next': "14",
                }
            },
            {
                'id': "14",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/wth14.mp3",
                'next': "15",
            },
            {
                'id': "15",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/wth15.mp3",
                'destination': {
                    'location': [40.7353, -74.0003],
                    'radius': 50,
                    'next': "16",
                }
            },
            {
                'id': "16",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/wth16.mp3",
                'next': "17",
            },
            {
                'id': "17",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/wth17.mp3",
                'destination': {
                    'location': [40.7351, -74.0017],
                    'radius': 50,
                    'next': "18",
                }
            },
            {
                'id': "18",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/wth18.mp3",
                'next': None,
            },
        ]
    },
    {
        'id': "McCarren",
        'name': "McCarren Park",
        'location': [40.721541, -73.954459],
        'moments': [
            {
                'id': "McCarren_Part1_Intro",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/McCarren_Part1_Intro.mp3",
                'destination': {
                    'location': [40.721541, -73.954459],
                    'radius': 50,
                    'next': "McCarren_Part1_Body",
                }
            },
            {
                'id': "McCarren_Part1_Body",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/McCarren_Part1_Body.mp3",
                'next': "McCarren_Part2_Intro",
            },
            {
                'id': "McCarren_Part2_Intro",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/McCarren_Part2_Intro.mp3",
                'destination': {
                    'location': [40.721310, -73.952704],
                    'radius': 50,
                    'next': "McCarren_Part2_Body",
                }
            },
            {
                'id': "McCarren_Part2_Body",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/McCarren_Part2_Body.mp3",
                'next': "McCarren_Part3_Intro",
            },
            {
                'id': "McCarren_Part3_Intro",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/McCarren_Part3_Intro.mp3",
                'destination': {
                    'location': [40.720297, -73.952676],
                    'radius': 50,
                    'next': "McCarren_Part3_Body",
                }
            },
            {
                'id': "McCarren_Part3_Body",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/McCarren_Part3_Body.mp3",
                'next': "McCarren_Part4_Intro",
            },
            {
                'id': "McCarren_Part4_Intro",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/McCarren_Part4_Intro.mp3",
                'destination': {
                    'location': [40.720374, -73.950732],
                    'radius': 50,
                    'next': "McCarren_Part4_Body",
                }
            },
            {
                'id': "McCarren_Part4_Body",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/McCarren_Part4_Body.mp3",
                'next': "McCarren_Part6_Intro",
            },
            {
                'id': "McCarren_Part6_Intro",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/McCarren_Part6_Intro.mp3",
                'destination': {
                    'location': [40.721730, -73.949997],
                    'radius': 50,
                    'next': "McCarren_Part6_Body",
                }
            },
            {
                'id': "McCarren_Part6_Body",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/McCarren_Part6_Body.mp3",
                'next': "McCarren_Part7_Intro",
            },
            {
                'id': "McCarren_Part7_Intro",
                'type': "TravelMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/McCarren_Part7_Intro.mp3",
                'destination': {
                    'location': [40.724430, -73.943465],
                    'radius': 50,
                    'next': "McCarren_Part7_Body",
                }
            },
            {
                'id': "McCarren_Part7_Body",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/McCarren_Part7_Body.mp3",
                'next': "McCarren_END",
            },
            {
                'id': "McCarren_END",
                'type': "ListenMoment",
                'audio': "http://storage.googleapis.com/sojourn-assets/McCarren_END.mp3",
                'next': None,
            },
        ],
    }
]

class BrowseService(BaseView):

    @Route('/api/0.0/get-sojourns/')
    def get(self):
        data = {}
        results = []
        for sojourn in SOJOURNS:
            results.append({
                'id': sojourn['id'],
                'name': sojourn['name'],
                'location': sojourn['location'],    
            })
        data['status'] = "OK"
        data['results'] = results
        return flask.jsonify(data)

    @Route('/api/0.0/get-sojourn-by-id/<id>/')
    def getById(self, id):
        for sojourn in SOJOURNS:
            if sojourn['id'] == id:
                return flask.jsonify({'status': "OK", 'result': sojourn})
        return flask.jsonify({'status': "NOT-FOUND"})