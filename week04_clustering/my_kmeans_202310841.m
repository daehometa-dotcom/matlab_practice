function [Final_label, my_CP] = my_kmeans_202310841(setdata, grp, class)

% [0단계: 초기 객체 선정]
my_CP = setdata(1:grp,:);

% [1단계: 객체 군집 배정]
my_label = [];

for kk = 1:1:length(setdata)

    tmp_set = setdata(kk,:);

    udist = zeros(grp,1);

    for jj = 1:1:grp
        udist(jj,1) = norm(tmp_set - my_CP(jj,:));
    end

    [sv, si] = sort(udist,'ascend');

    my_label(kk,1) = class(si(1));

end

Final_label = [];
chk = 1;
loop = 0;

while(chk)

    loop = loop + 1;

    % 새로운 중심 좌표 계산
    for kk = 1:1:grp

        idx = find(my_label == class(kk));
        tmp_data = setdata(idx,:);

        my_CP(kk,:) = mean(tmp_data);

    end

    % 새로운 중심으로 데이터 재배정
    my_label_new = [];

    for kk = 1:1:length(setdata)

        tmp_set = setdata(kk,:);

        udist = zeros(grp,1);

        for jj = 1:1:grp
            udist(jj,1) = norm(tmp_set - my_CP(jj,:));
        end

        [sv, si] = sort(udist,'ascend');

        my_label_new(kk,1) = class(si(1));

    end

    % 이전 군집 결과와 비교
    idx = find(my_label_new ~= my_label);

    if length(idx) == 0

        chk = 0;
        Final_label = my_label_new;
        break;

    else

        my_label = my_label_new;

    end

end

end