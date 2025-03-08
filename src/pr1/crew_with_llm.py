from litellm import completion 
from crewai.flow.flow import Flow , start , listen
from dotenv import load_dotenv
import os
load_dotenv()
os.getenv("GEMINI_API_KEY")


class SimpleFlow(Flow):
    @start()
    def generate_country_name(self):
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[
                {
                    "role": "user",
                    "content": "generate a random country name from asia"
                }
            ]
        )   
        result = response["choices"][0]["message"]["content"]
        print(result)
        return result
    @listen(generate_country_name)
    def generate_city_name(self,country_name):
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[
                {
                    "role": "user",
                    "content": f"generate a city name from {country_name}"
                }
            ]               
        )   
        result = response["choices"][0]["message"]["content"]
        print(result)
        return result
    @listen(generate_city_name)
    def generate_fun_fact(self, result):
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[
                {
                    "role": "user",
                    "content": f"generate some fun fact about {result}."
                }
            ]
        )   
        result = response["choices"][0]["message"]["content"]
        print(result)
        return result
    @listen(generate_fun_fact)
    def save_file(self , result):
        with open("city_name_and_fun_fact.txt", "w") as file:
            file.write(result)
        print("File saved successfully.")   
        
def kickoff():
    flow = SimpleFlow()
    flow.kickoff()
    
