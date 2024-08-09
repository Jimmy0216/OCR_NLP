# import os
# from fastapi import FastAPI, UploadFile, File, HTTPException
# from fastapi.responses import JSONResponse
# from paddleocr import PaddleOCR
# from PIL import Image
# import io
# import numpy as np

# app = FastAPI()

# # PaddleOCR 모델 초기화
# ocr_model = PaddleOCR(use_angle_cls=True, lang='korean')

# def ocr_image_paddle(image: np.ndarray) -> str:
#     """
#     주어진 numpy 이미지 배열을 사용해 PaddleOCR을 사용해 텍스트를 추출하는 함수
#     """
#     result = ocr_model.ocr(image, cls=True)
#     extracted_text = ""
#     for line in result:
#         for word_info in line:
#             extracted_text += word_info[1][0] + " "
#     return extracted_text.strip()

# @app.post("/ocr")
# async def ocr(file: UploadFile = File(...)):
#     if not file.filename.endswith(('.png', '.jpg', '.jpeg')):
#         raise HTTPException(status_code=400, detail="지원되지 않는 파일 형식입니다. PNG, JPG, JPEG 파일만 지원됩니다.")
    
#     try:
#         image_data = await file.read()
#         image = Image.open(io.BytesIO(image_data))
#         image = np.array(image)
#         text = ocr_image_paddle(image)
#         return JSONResponse(content={"extracted_text": text})
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

import os
from paddleocr import PaddleOCR
from PIL import Image
import numpy as np

# PaddleOCR 모델 초기화
ocr_model = PaddleOCR(use_angle_cls=True, lang='korean')

def ocr_image_paddle(image_path: str) -> str:
    """
    주어진 이미지 파일 경로를 사용해 PaddleOCR로 텍스트를 추출하는 함수
    """
    image = Image.open(image_path)
    image = np.array(image)
    result = ocr_model.ocr(image, cls=True)
    extracted_text = ""
    for line in result:
        for word_info in line:
            extracted_text += word_info[1][0] + " "
    return extracted_text.strip()

if __name__ == "__main__":
    # 이미지 파일 경로 지정
    image_path = r"C:\jaemin\dev\OCR_NLP\123.jpg"
    
    # 파일 존재 여부 확인
    if not os.path.exists(image_path):
        print(f"오류: 파일이 존재하지 않습니다: {image_path}")
    else:
        # OCR 실행
        text = ocr_image_paddle(image_path)
        
        # 결과 출력
        print("추출된 텍스트:")
        print(text)