#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import cv2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def dist_thresholding(des1, des2, threshold_value) -> list:
    bf = cv2.BFMatcher()

    matchesRes = []
    matches = bf.knnMatch(des1, des2, 100)
    for match in matches:
        temp = []
        for each in match:
            if each.distance < threshold_value:
                temp.append(each)
        matchesRes.append(temp)

    return matchesRes

def nn(des1, des2, threshold_value) -> list:
    bf = cv2.BFMatcher()

    matchesRes = []
    matches = bf.knnMatch(des1, des2, 100)
    matches = [knnMatch[0] for knnMatch in matches]

    for match in matches:
        temp = []
        if match.distance < threshold_value:
            temp.append(match)
        elif threshold_value == -1:
            temp.append(match)
        matchesRes.append(temp)

    return matchesRes


def nndr(des1, des2, threshold_value) -> list:
    bf = cv2.BFMatcher()

    matchesRes = []
    matches = bf.knnMatch(des1, des2, k=2)

    for m in matches:
        temp = []
        if m[0].distance < threshold_value * m[1].distance:
            temp.append(m[0])
        matchesRes.append(temp)

    return matchesRes

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vim:set et sw=4 ts=4:
