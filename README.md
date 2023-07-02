# 2023-1-OSSP2-AntiGPT-9
2023년, 1학기, 공개SW프로젝트, 02분반, 챗GPT가 지어준 이름이 마음에 안 든 조, 9조

# Encoder-Decoder based jeju translation web service


---
<p align="center">
  <br>
  <img src="https://github.com/leadawon/2023-1-OSSP2-AntiGPT-9/blob/main/4readme/maindoor.png">
  <br>
  
  [pdf](https://github.com/leadawon/2023-1-OSSP2-AntiGPT-9/blob/main/4readme/ossp_final.pdf) < - PLEASE CLICK THIS TO SEE MORE DETAILS!
  
</p>


## 프로젝트 소개

### what is purpose of the project?
<p align="center"> 
<br>
  <img src="https://github.com/leadawon/2023-1-OSSP2-AntiGPT-9/blob/main/4readme/systemstructure.png">
<br>
</p>
제주방언을 받으면 표준어를 반환하는 api 서버를 구현하고 chatgpt api와 결합하여 방언으로 chatgpt와 대화할 수 있는 서비스를 배포합니다.


[AIhub](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100) dataset에서 train, test 용 데이터를 정제하고 지도학습에 사용했습니다.

---
<p align="center"> 
<br>
  <img src="https://github.com/leadawon/2023-1-OSSP2-AntiGPT-9/blob/main/4readme/encoderdecodercapture.png">
<br>
</p>

pretrained model로 [monologg](https://github.com/monologg)님의 [kobert](https://github.com/monologg/KoBERT-Transformers)와 sktai의 [kogpt2](https://github.com/SKT-AI/KoGPT2)를 사용했습니다.
  
---
  
500 문장에 대해서 평균 [BLEU score](https://en.wikipedia.org/wiki/BLEU)는 60점대로 수렴했습니다. 추가적으로 [방언 사용자](https://github.com/leadawon/2023-1-OSSP2-AntiGPT-9/blob/main/4readme/realdialectpdf.pdf)에게 59문장의 번역결과 테스트를 부탁드렸고 데이터의 전처리가 부족했다는 피드백을 얻었습니다.

---
  
<p align="center">
<br>
<img src="https://github.com/leadawon/2023-1-OSSP2-AntiGPT-9/blob/main/4readme/apiserver.png">
<br>
</p>

api 서버에게 방언으로 요청을 보내면 번역된 결과를 얻을 수 있습니다.

---


<p align="center">
<br>
<img src="https://github.com/leadawon/2023-1-OSSP2-AntiGPT-9/blob/main/4readme/webserver.png">
<br>
</p>

chatgpt 화면과 유사하게 웹을 구현했습니다.
방언을 입력하면서 chatgpt와 대화를 할 수 있습니다.

<br>

## 기술 스택

|   Python   |   Pytorch  |  Django  | Transformers |

<br>
  
</p>

## 성능을 높이기 위한 방법

### 사전 학습모델 사용

hugging face 라이브러리에서 pretrained model을 사용함.

kobert, kogpt2 를 기반으로 한국어 사전학습 모델을 번역모델로 finetuning

### tokenizer update

방언의 형태소를 토크나이저가 인식할 수 있도록 방언 형태소를 토크나이저에 추가함.

수작업으로 500개의 문장을 분석했다.

공통적으로 반복되는 체언의 어미나 어근의 접사를 토크나이저에 추가했다.

0kt 한국어 형태소 분석기를 통해서 나머지 형태소를 추가했다.

### hyper parameter tuning

grid search로 하이퍼파라미터를 튜닝했다.

<br>

## 배운 점 & 아쉬운 점

aihub에서 제공하는 데이터에서 방언에서 표준어로 제대로 번역되지 않은 문장이 있었다. 제주 방언에 대한 전문성이 없어서 이것을 일찍 파악하지 못했다.

실제 방언 사용자에게 피드백을 받았을때 위와 같은 인사이트를 얻었고 역시 도메인 지식을 잘 아는것이 중요하다고 생각했다.

---

사전학습 모델의 장점을 살리지 못했다. encoder로 kobert, decoder로 kogpt2를 사용했지만 skt에서 학습시킨 가중치를 유의미 하게 사용할 수 없었다.

애초에 인코더-디코더 모델로 사전학습된 kobert를 사용했다면 더 좋았을 것 같다.

---
