import requests 
import os


def download_url(x, f):
     i = 0  
     while i < 5: 
       
      for a in x:
       r = requests.get(x[i]) 

       with open( f[i],'wb') as file: 
        file.write(r.content) 

       i += 1 

def main():
 x = ['https://www.nbcnews.com/health/health-news/get-back-track-new-years-resolutions-rcna136787',
     'https://www.nbcnews.com/health/bidens-memory-issues-draw-attention-neurologists-weigh-rcna138135',
     'https://www.nbcnews.com/health/health-news/oregons-first-case-human-plague-8-years-likely-came-cat-rcna138090',
     'https://www.nbcnews.com/health/health-news/robotic-device-burned-womans-small-intestine-surgery-lawsuit-alleges-rcna137998',
     'https://www.nbcnews.com/health/health-news/fungus-sparked-deadly-meningitis-outbreak-aggressively-attacked-brains-rcna137780']

 f = ["Article1.txt", "Article2.txt", "Article3.txt", "Article4.txt", "Article5.txt"]

 download_url(x, f)

if __name__=="__main__":
    main()
