import pandas as pd
from Levenshtein import distance as levenshtein_distance

class SimpleChatBot:
    def __init__(self, filepath):
        self.questions, self.answers = self.load_data(filepath)

    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data['Q'].tolist()
        answers = data['A'].tolist()
        return questions, answers

    def find_best_answer(self, input_sentence):
        # 입력 문장과 학습 질문들 간의 레벤슈타인 거리 계산
        distances = [
            levenshtein_distance(input_sentence, q)
            for q in self.questions
        ]
        # 최소 거리인 질문의 인덱스 찾기
        best_match_index = distances.index(min(distances))
        # 인덱스의 답변을 리턴
        return self.answers[best_match_index]

if __name__ == '__main__':
    filepath = 'ChatbotData.csv'
    chatbot = SimpleChatBot(filepath)

    print("챗봇에 질문을 입력하세요. (종료하려면 '종료' 입력)")
    while True:
        input_sentence = input('You: ')
        if input_sentence.strip().lower() == '종료':
            break
        response = chatbot.find_best_answer(input_sentence)
        print('Chatbot:', response)
