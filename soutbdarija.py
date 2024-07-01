import gtts
from playsound import playsound
import os

def darija_tts(text, output_file="output.mp3"):
    # Use 'ar' (Arabic) as the language code
    tts = gtts.gTTS(text, lang='ar')
    tts.save(output_file)
    #playsound(output_file)
    #os.remove(output_file)  # Remove the file after playing

# Example usage
darija_text = """

"دابا غادي نخدم لاوديو ريفيو على لتراك "بوبيت مان" ديال لمورفين.
لتراك كايبدا بواحد لانترو مخوفة، و كايوري بلي غايكون عندنا واحد لبيرسوناج غريب سميتو "بوبيت مان".
لارتيست كايغني بدارجة و فرنساوية، و كايهدر على بزاف ديال لمواضيع معقدة: لحياة، لمشكيل ديال لمجتمع، و كيفاش لإنسان كايحاول يلقى لمعنى ف هاد لعالم صعيب.
لتراك عندو واحد لبيت قوي لي كايمشي مع لي بارول. لارتيست كايعبر على لأفكار ديالو بواحد الطريقة مؤثرة و عميقة، و كايوصف لينا لحياة ديال الشعب و لمشكيلات لي كايواجهوهم.
لتراك كاين فيه بزاف ديال لميتافور و لاستعارات ف لي بارول، لي كايعطيو لتراك واحد لقيمة فنية كبيرة. لارتيست كايهدر على لواقع و لأحلام، و كيفاش لإنسان كايدير باش يعيش ف هاد لمجتمع"  # "As-salaam-alaikum" (Hello) in Darija
"""
darija_tts(darija_text)