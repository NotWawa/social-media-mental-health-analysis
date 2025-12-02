# Social Media & Mental Health Analysis 🧠📱

## 📌 Project Overview
I deleted Instagram and TikTok to improve my productivity, but I wanted to see if the data supported my decision. This project analyzes 500 users to determine how different platforms, screen time, and sleep habits impact mental health scores.

[Dashboard Preview](https://public.tableau.com/views/mh_dashboard/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)


## 🔍 Key Findings
* **The "Sleep Killer":** Strong negative correlation between Screen Time and Sleep Quality.
* **Platform Impact:** Instagram users reported the lowest happiness and sleep scores in the dataset.
* **Model Accuracy:** Random Forest Regressor predicted mental health scores with high accuracy (See `mh_predict.py`).

## 🛠 Tech Stack
* **Python:** Data cleaning (Pandas) and Machine Learning (Scikit-Learn).
* **SQL:** Data querying and segmentation.
* **Tableau:** Interactive dashboard design.

## 📂 File Structure
* `mh_predict.py`: The Random Forest model used to predict mental health scores.
* `smmh_clean.csv`: The cleaned dataset used for analysis.
* `Social_Media_Analysis.twbx`: The Tableau workbook file.
