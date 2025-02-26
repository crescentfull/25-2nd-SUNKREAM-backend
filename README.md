#  SHOEKREAM Project

![shokreammain](https://user-images.githubusercontent.com/78721108/139569482-db28b424-c233-4df5-9520-4da68e528439.gif)

- PREMIUM BIIDINGS

## 🎇 팀명 : shoekream - 슈크림

> 의류 경매 서비스를 제공하는 [KREAM](https://kream.co.kr/)을 모티브로 제작하게 된 SHOE-KREAM 팀의 프론트엔드 레포지토리 입니다.
> 짧은 프로젝트 기간동안 개발에 집중해야 하므로 디자인/기획 부분만 클론했습니다.
> 개발은 초기 세팅부터 전부 직접 구현했으며, 백앤드와 연결하여 실제 사용할 수 있는 서비스 수준으로 개발할 수 있도록 2주간 고군분투 하였습니다.

### 프로젝트 선정이유
- 조사결과, 해당 사이트의 경매 입찰 기능과 결제 플로우, 차트 구현, 상품리스트 필터 구현 등 배울 점이 많다고 판단하여 선정하게 되었습니다.

## 📅 개발 기간 및 개발 인원

- 개발 기간 : 2021/10/18 ~ 2021/10/29
- 개발 인원 <br/>
 👨‍👧‍👦 **Front-End** 4명 : 김현진, 박산성, 이선호, 하상영<br/>
 👨‍👧‍👦 **Back-End** 3명 : 박치훈, 양가현, 송영록<br/>
- [Back-end github 링크](https://github.com/wecode-bootcamp-korea/25-2nd-SUNKREAM-backend)

## 🎬 프로젝트 구현 영상

- 🔗 [구현영상] : https://youtu.be/N63MUdDmDFI

## ⚙ 적용 기술
- **Front-End** : HTML5, CSS3, React, SASS, JSX
- **Back-End** : Python, Django, MySQL, jwt, bcypt, AWS RDS, AWS EC2
- **Common** : Git, Github, Slack, Trello, Postman or Insomnia

## 🗜 [데이터베이스 Diagram(클릭 시 해당 링크로 이동합니다)](https://www.erdcloud.com/d/6Kq4rCsrgRkjcfZxk)
![kream](https://user-images.githubusercontent.com/78721108/139569506-39104ecf-7060-4aa0-8d45-c834bc1a4174.png)

## 💻 구현 기능

Endpoint documentation - [Postman API](https://documenter.getpostman.com/view/17773566/2s7ZE5r4jy)

### BACKEND

#### 송영록

> 상세 페이지
- 구매, 판매 가격 입찰데이터 join하여 filter로 출력
- 제품이 없을 경우 'product_id_not_exist' 반환
- 주문 목록은 주문일시가 빠른 시간부터 정렬
- 좋아요(관심상품) 클릭 수를 len()함수를 써서 전체 숫자 출력
- 제품 ID, 제품명, 브랜드명, 제품 발매가격, 모델 번호, 해당 제품 이미지, 현재 가격(입찰 없을 경우 none), 구매가격, 판매가격, 총 관심상품 등록 수  >>> dictionary json 반환

> 상품 리스트 출력 API(ProductView)
- 프론트 요청시 제품 데이터 40개 제한 출력(offset,limit)
- 제품 ID, 브랜드명, 제품명, 썸네일이미지, 제품 가격(살떄), 제품 발매가격 >>> dictionary json 반환

> 브랜드 리스트 출력 API(BrandView)
- 메인 페이지, 제품 페이지 상단 브랜드 출력을 위하여 API 작성


## ❗ Reference
- 이 프로젝트는 [KREAM](https://kream.co.kr/) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 모두는 copyright free 사이트들의 이미지들을 취합 및 canva 에서 직접 제작한 이미지들로 제작되었습니다.
